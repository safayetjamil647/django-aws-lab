from django.urls import path, reverse
from wagtail.core import hooks
from wagtail.admin.menu import MenuItem, SubmenuMenuItem
from wagtail.contrib.modeladmin.menus import SubMenu
from .views import index, ec2_index, download_file, launch_instances,get_running_instances, linux_index,aws_playground


@hooks.register('register_admin_urls')
def register_calendar_url():
    return [
        path('resources/', index, name='resource'),
        path('resources/ec2/', ec2_index, name='ec2'),
        path('resources/ec2/keypair', download_file, name='key'),
        path('resources/ec2/launch/', launch_instances, name='launcher'),
        path('resources/ec2/all_instances/', get_running_instances, name='allinstances'),
        path('resources/aws_ground/', aws_playground, name='playground'),
        path('resources/linux/', linux_index, name='linux'),
    ]


@hooks.register('register_admin_menu_item')
def register_calendar_menu_item():
    menu_items = [
        MenuItem('AWS Resource', reverse('ec2'), icon_name='date'),
        MenuItem('AWS Playground', reverse('playground'), icon_name='date'),
        MenuItem('Linux Terminal', reverse('linux'), icon_name='date'),
    ]
    return SubmenuMenuItem('Resource Manager', SubMenu(menu_items), classnames='icon icon-date')


@hooks.register('construct_main_menu')
def hide_snippets_menu_item(request, menu_items):
    menu_items[:] = [item for item in menu_items if item.name != 'reports']
