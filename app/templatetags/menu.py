from django import template
from ..models import MenuItems
from collections import defaultdict

register = template.Library()


@register.tag
def draw_menu(parser, token):
    menu_name = token.split_contents()[1]

    return SiteMenu(menu_name)


class SiteMenu(template.Node):
    def __init__(self, menu_name):
        self.menu_name = menu_name

    def render(self, context):
        menu = MenuItems.objects.filter(menu__name=self.menu_name).all()
        tree = self.astree(menu, 'parent')
        display = 'block'
        active = ''

        def parse_tree(tree, lvl):
            res = []
            nonlocal display
            nonlocal active

            for item in tree[lvl]:
                if item.url == context['request'].path:
                    active = 'active'

                res.append('<li class="{}"><a href="{}">{}</a></li>'.format(active, item.url, item.name))

                if item in tree.keys():
                    res.append(
                        ''.join(['<ul style="display: {}">'.format(display), parse_tree(tree, item), '</ul>'])
                    )
                    if item.url == context['request'].path:
                        display = 'none'
            return ''.join(res)

        menu = parse_tree(tree, None)

        return menu

    @staticmethod
    def astree(items, attribute):
        parent_map = defaultdict(list)
        for item in items:
            parent_map[getattr(item, attribute)].append(item)

        return parent_map
