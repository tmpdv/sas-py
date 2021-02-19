from django.core.paginator import Paginator


def to_page(object_list, num, size):
    paginator = Paginator(object_list, size)
    return dict(
        pageNumber=num,
        size=size,
        totalPages=paginator.num_pages,
        elementList=paginator.get_page(num).object_list
    )


def to_page_default_size(object_list, num):
    return to_page(object_list, num, 10)


def to_first_page_default_size(object_list):
    return to_page(object_list, 1, 10)


