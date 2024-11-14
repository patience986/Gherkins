from pytest_bdd import scenarios, given,when,then
scenarios('Gherkin/tests/features/navigating.feature')

@given('I am on the Home page')  
def i_am_on_the_home_page():
    print('navigating the home page')

@when('I click on the "About" link')
def i_click_on_the_about_link():
    print('about clicked')

@then('I should be redirected to the About page')
def i_should_be_redirected_to_the_about_page():
    print('about page loaded')