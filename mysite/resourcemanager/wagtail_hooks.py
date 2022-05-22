from django.urls import path, reverse
from wagtail.core import hooks
from wagtail.admin.menu import MenuItem, SubmenuMenuItem
from wagtail.contrib.modeladmin.menus import SubMenu
from .views import index, ec2_index


@hooks.register('register_admin_urls')
def register_calendar_url():
    return [
        path('resources/', index, name='resource'),
        path('resources/ec2/', ec2_index, name='ec2'),
    ]


@hooks.register('register_admin_menu_item')
def register_calendar_menu_item():
    menu_items = [
        MenuItem('More Resources', reverse('resource'), icon_name='date'),
        MenuItem('EC2', reverse('ec2'), icon_name='date'),
    ]
    return SubmenuMenuItem('Resource Manager', SubMenu(menu_items), classnames='icon icon-date')


@hooks.register('construct_main_menu')
def hide_snippets_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != 'reports']
