from behave import given, when, then
from booking.apply_filtrations import ApplyFiltration
from booking.bookings import Booking

book = Booking()
filtration = ApplyFiltration()


@given('User opens the browser and goes to the home page')
def open_browser_and_home_page(context):
    context.book = book.open_home_page()


@when('User selects the search criteria for hotels')
def search_criteria(context):
    context.book = book.change_currency(currency='USD')
    context.book = book.select_place(location='New York')
    context.book = book.check_in_and_check_out_date(check_in="2022-05-16", check_out="2022-05-24")
    context.book = book.select_guest_count(count=2)
    context.book = book.search_hotels()


@then('User makes filtration and sees the all filtered hotels')
def make_filtration(context):
    context.filtration = filtration.star_rating(star=3)
    context.filtration = filtration.sort_price_lowest_to_highest()
    context.filtration = filtration.close_browser()
