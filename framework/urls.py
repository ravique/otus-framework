import framework.views

urls = {
    '/':
        {'view': framework.views.mainpage_view, 'allowed_methods': ('GET', 'POST')},
    '/books':
        {'view': framework.views.books_list_view, 'allowed_methods': ('GET',)},
    '/disks':
        {'view': framework.views.disks_list_view, 'allowed_methods': ('GET',)},
    '/forbidden_to_all':
        {'view': framework.views.base_view, },
}
