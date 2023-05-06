from django import template
from menu.models import MenuItem, Menu

register = template.Library()


@register.inclusion_tag('menu.html', takes_context=True)
def draw_menu(context, menu_name):
    current_url = context['request'].path
    menu_items = MenuItem.objects.all() \
        .select_related('menu', 'parent') \
        .filter(menu__name=menu_name) \
        .order_by('parent_id')

    # перебираем элементы меню, чтобы отобразить в дальнейшем в виде дерева
    prepare_menu_items = []
    for item in menu_items:
        if item.parent_id is None:
            prepare_menu_items.append(item)
            # добавляем меню если оно не имеет потомков
        else:
            # ищем родителя объекта и добавляем "под ним" значение
            for i, sort_item in enumerate(prepare_menu_items):
                if item.parent_id == sort_item.id:
                    prepare_menu_items.insert(i + 1, item)

    active = True
    parent_last_id = prepare_menu_items[0].id
    root_id = prepare_menu_items[0].id

    for item in prepare_menu_items:
        if current_url == item.url:
            parent_last_id = item.parent_id


    tree = []
    last_active_id = prepare_menu_items[0].id

    for item in prepare_menu_items:
        tree.append({
            'id': item.id,
            'name': item.name,
            'menu': menu_name,
            'parent': item.parent_id,
            'url': item.url if item.url != '' else '/',  # либо url либо /
            'active': active,
        })

        # matching last_active_id
        if active:
            last_active_id = item.id
        if item.url == current_url \
                or item.url == '' and current_url == '/':
            active = False



    print(current_url, parent_last_id)
    print(last_active_id)

    for item in tree:
        if item['parent'] == root_id or item['parent'] == parent_last_id:
            item['active'] = True
        else:
            item['active'] = False


    for item in tree:
        if  item['url'] == current_url or \
            item['parent'] is None or \
            item['parent'] == last_active_id:
            item['active'] = True
            parent_id = item['parent']
            while parent_id is not None:
                for parent_item in tree:
                    if parent_item['id'] == parent_id:
                        parent_item['active'] = True
                        parent_id = parent_item['parent']
                        break
                else:
                    parent_id = None

    return {
        'menu_tree': tree,
    }


@register.simple_tag(takes_context=True)
def render_menu(context, menu_tree, current_item=None):
    result = ''
    for item in menu_tree:
        if item['parent'] == current_item and item['active'] == True:
            result += f'<li><a href="{item["url"]}" {"class=menuitem" if item["active"] else ""}>{item["name"]}</a>'
            sub_menu = render_menu(context, menu_tree, item['id'])
            if sub_menu:
                result += f'<ul>{sub_menu}</ul>'
            result += '</li>'
    return result
