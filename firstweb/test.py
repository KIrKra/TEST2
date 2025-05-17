from news.models import News
from news.forms import NewsForm


print(News.objects.all())
form = NewsForm()
print(form)