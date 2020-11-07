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
    key = None

    def __init__(self, name, path):
        self.name = name
        self.key = self.name.lower()
        self.path = path


themes = {
    "bootstrap": Theme("Bootstrap", "common/css/themes/bootstrap_4_5_3/bootstrap.min.css"),
    "cosmo": Theme("Cosmo", "common/css/themes/cosmo_4_5_2/bootstrap.min.css"),
    "cosmo": Theme("Cosmo", "common/css/themes/cosmo_4_5_2/bootstrap.min.css"),
    "cyborg": Theme("Cyborg", "common/css/themes/cyborg_4_5_2/bootstrap.min.css"),
    "darkly": Theme("Darkly", "common/css/themes/darkly_4_5_2/bootstrap.min.css"),
    "flatly": Theme("Flatly", "common/css/themes/flatly_4_5_2/bootstrap.min.css"),
    "material": Theme("Material", "common/css/themes/colormind_material/colormind-material-dashboard.css"),
    "minty": Theme("Minty", "common/css/themes/minty_4_5_2/bootstrap.min.css"),
    "paper": Theme("Paper", "common/css/themes/colormind_paper/colormind-paper-dashboard.css"),
    "sandstone": Theme("Sandstone", "common/css/themes/sandstone_4_5_2/bootstrap.min.css"),
    "slate": Theme("Slate", "common/css/themes/slate_4_5_2/bootstrap.min.css"),
    "superhero": Theme("Superhero", "common/css/themes/superhero_4_5_2/bootstrap.min.css"),
}


class Functions:

    @staticmethod
    def build_page_context(page, request):
        theme = themes["bootstrap"]
        if "theme" in request.session:
            theme = themes[request.session["theme"]]

        context = {
                    "page": page,
                    "user": request.user,
                    "authenticated": request.user.is_authenticated,
                    "remove_tag_list": "strong b em i img",
                    "themes": themes.values(),
                    "theme": theme
                }

        if request.user.is_authenticated:
            context["gravatar"] = Gravatar.url(request.user.email)

        return context

    @staticmethod
    def set_theme(request, theme):
        request.session["theme"] = theme
