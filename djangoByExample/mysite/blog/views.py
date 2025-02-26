from django.db.models import Count
# from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.postgres.search import TrigramSimilarity
# from django.http import Http404
from django.views.generic import ListView
from django.views.decorators.http import require_POST
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail

from taggit.models import Tag

from .models import Post, Comment
from .forms import EmailForm, CommentForm, SearchForm


# Create your views here.
def post_list(request, tag_slug=None):
    post_list = Post.published.all()

    tag = None
    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        post_list = post_list.filter(tags__in=[tag])

    paginator = Paginator(post_list, 3)
    page_number = request.GET.get('page', 1)

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request,
                  'blog/post/list.html',
                  {'posts': posts,
                   'tags': tag})


class PostList(ListView):
    model = Post
    context_object_name = "posts"
    paginate_by = 3
    template_name = "blog/post/list.html"

    def get_queryset(self):
        query = None
        if 'query' in self.request.GET:
            form = SearchForm(self.request.GET)
            if form.is_valid():
                query = form.cleaned_data['query']

            # 트라이그램 검색
            return (Post.published
                    .annotate(similarity=TrigramSimilarity('title', query), )
                    .filter(similarity__gte=0.1)
                    .order_by('-similarity'))
        return Post.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SearchForm(self.request.GET)
        return context



def post_detail(request, year, month, day, post):
    # try:
    #     post = Post.objects.get(pk=id)
    # except Post.DoesNotExist:
    #     raise Http404("Post does not exist")
    post = get_object_or_404(Post,
                             status=Post.Status.PUBLISHED,
                             slug=post,
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    comments = post.comments.filter(active=True)

    form = CommentForm()

    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', '-publish')[:2]


    return render(request,
                  'blog/post/detail.html',
                  {'post': post,
                   'comments': comments,
                   'form': form,
                   'similar_posts': similar_posts})

def post_share(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent = False

    if request.method == 'POST':
        form = EmailForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            #이메일 전송
            subject = f"{cd['name']} recommends you read {post.title}."
            post_url = request.build_absolute_uri(post.get_absolute_url())
            message = (f"Read {post.title} at {post_url}\n\n "
                       f"{cd['name']}'s comments: {cd['comments']}")
            send_mail(subject, message, cd['email'], [cd['to']])
            sent = True
    else:
        form = EmailForm()
    return render(request,
                  'blog/post/share.html',
                  {'post': post, 'form': form, 'sent': sent})

@require_POST
def post_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    comment = None

    form = CommentForm(data=request.POST)
    if form.is_valid():
        comment = form.save(commit=False)
        comment.post = post
        comment.save()

    return render(request,
                  'blog/post/comment.html',
                  {'post': post, 'form':form, 'comment': comment})



def post_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # 벡터 검색
            # search_vector = (SearchVector('title', weight='A') +
            #                  SearchVector('body', weight='B'))
            # search_query = SearchQuery(query)
            # results = (Post.published
            #            .annotate(search=search_vector,
            #                      rank=SearchRank(search_vector, search_query))
            #            # .filter(search=search_query)
            #            .filter(rank__gte=0.3)
            #            .order_by('-rank'))

            # 트라이그램 검색
            results = (Post.published
                       .annotate(similarity=TrigramSimilarity('title', query),)
                       .filter(similarity__gte=0.1)
                       .order_by('-similarity'))


    return render(request, 'blog/post/search.html',
                  {'form': form, 'query': query, 'results': results})