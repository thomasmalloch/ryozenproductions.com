import hashlib
import urllib.parse


class Gravatar:

    @staticmethod
    def url(email, size=40):
        md5 = hashlib.md5(email.lower().encode("utf-8")).hexdigest()
        query = urllib.parse.urlencode({'d': 'wavatar', 's': str(size)})
        return "https://www.gravatar.com/avatar/%s?%s" % (md5, query)


class Theme:
    name = None
    path = None

    def __init__(self, name, path):
        self.name = name
        self.path = path


themes = {
    "bootstrap": Theme("Bootstrap", "news/css/themes/bootstrap/bootstrap.min.css"),
    "cyborg": Theme("Cyborg", "news/css/themes/cyborg/bootstrap.min.css"),
    "darkly": Theme("Darkly", "news/css/themes/darkly/bootstrap.min.css"),
    "darkster": Theme("Darkster", "news/css/themes/darkster/theme.min.css"),
    "greyson": Theme("Greyson", "news/css/themes/greyson/theme.min.css"),
    "monotony": Theme("Monotony", "news/css/themes/monotony/theme.min.css"),
    "sandstone": Theme("Sandstone", "news/css/themes/sandstone/bootstrap.min.css"),
    "slate": Theme("Slate", "news/css/themes/slate/bootstrap.min.css"),
    "solar": Theme("Solar", "news/css/themes/solar/bootstrap.min.css"),
    "superhero": Theme("Sandstone", "news/css/themes/superhero/bootstrap.min.css"),
    "tequila": Theme("Tequila", "news/css/themes/tequila/theme.min.css"),
}


class Functions:

    @staticmethod
    def build_page_context(page, request):
        theme = themes["darkly"]
        if "theme" in request.session:
            theme = themes[request.session["theme"]]

        context = {
                    "page": page,
                    "user": request.user,
                    "authenticated": request.user.is_authenticated,
                    "remove_tag_list": "strong b em i img",
                    "themes": themes,
                    "theme": theme
                }

        if request.user.is_authenticated:
            context["gravatar"] = Gravatar.url(request.user.email)

        return context

    @staticmethod
    def set_theme(request, theme):
        request.session["theme"] = theme
