from django.contrib.sitemaps import Sitemap
from .models import Specialty
from .models import Teacher


class SpecialtySitemap(Sitemap):
    def items(self):
        return Specialty.objects.all()

    def lastmod(self, obj):
        return obj.lastedit_date

    def location(self, obj):
        return f"/specialty/{obj.id}/"


class TeacherSitemap(Sitemap):
    def items(self):
        return Teacher.objects.all()

    def lastmod(self, obj):
        return obj.lastedit_date

    def location(self, obj):
        return f"/teacher/{obj.id}/"