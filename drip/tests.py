from datetime import datetime

from django.test import TestCase
from django.test import Client
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.models import User


from drip.models import DripSubscriber, DripSubscriberList, DripMessage
from drip.forms import *
from drip.tracking import tracking_string

#command: python3 manage.py test --verbosity=2


class DripSubscriberListUnitTest(TestCase):
    """
    DripSubscriberList model unit test
    """


    def setUp(self):
    
        self.drip_subscriber_list = DripSubscriberList.objects.create(
            name="test"
            )


    def test_name_field_type(self):
        self.assertIsInstance(self.drip_subscriber_list.name, str)


    def test_name_field_value(self):
        self.assertTrue(self.drip_subscriber_list.name == "test")


    def test_created_field(self):
        self.assertIsInstance(self.drip_subscriber_list.created, datetime)


class DripSubscriberUnitTest(TestCase):
    """
    DripsSubscriber model unit test
    """


    def setUp(self):

        self.drip_subscriber = DripSubscriber.objects.create(
            email="a@a.com",
            funnel_entry_point="URI: test, location: test",
        )



    def test_email_field_type(self):
        self.assertIsInstance(self.drip_subscriber.email, str)


    def test_email_field_value(self):
        self.assertEqual(self.drip_subscriber.email, "a@a.com")


    def test_funnel_entry_point_field_type(self):
        self.assertIsInstance(self.drip_subscriber.funnel_entry_point, str)


    def test_funnel_entry_point_field_value(self):
        self.assertEqual(self.drip_subscriber.funnel_entry_point, "URI: test, location: test")


    def test_active_field_type(self):
        self.assertIsInstance(self.drip_subscriber.active, bool)


    def test_active_field_value(self):
        self.assertEqual(self.drip_subscriber.active, True)


    def test_created_field(self):
        self.assertIsInstance(self.drip_subscriber.created, datetime)


    def test_drip_subscriber_list_field_value(self):
        self.assertTrue(self.drip_subscriber.drip_subscriber_lists.first() == None)


class DripMessageUnitTest(TestCase):
    """
    DripMessage model unit tests
    """


    def setUp(self):

        self.user = User.objects.create(
            username="test",
            password="hello_world",
            email="test@test.com",
            first_name="hello",
            last_name="world"
        )

        self.drip_message = DripMessage.objects.create(
            title="test message",
            body="test body",
            author=self.user
        )


    def test_title_field_value_is_string_type(self):
        self.assertIsInstance(self.drip_message.title, str)


    def test_title_field_value(self):
        self.assertEqual(self.drip_message.title, "test message")


    def test_body_field_value_is_string_type(self):
        self.assertIsInstance(self.drip_message.body, str)


    def test_body_field_value(self):
        self.assertEqual(self.drip_message.body, "test body")


    def test_author_field_is_user_instance(self):
        self.assertIsInstance(self.drip_message.author, User)


    def test_author_field_user_email_is_the_same(self):
        self.assertEqual(self.drip_message.author.email, self.user.email)


    def test_created_field_is_datetime_instance(self):
        self.assertIsInstance(self.drip_message.created, datetime)


    def test_published_field_is_bool_type(self):
        self.assertIsInstance(self.drip_message.published, bool)


    def test_published_field_value_default_is_false(self):
        self.assertTrue(self.drip_message.published == False)


class DripIntegrationTest(TestCase):
    """
    Integrations tests for drip.views
    """


    def setUp(self):
        self.client = Client()

        self.user = User.objects.create_user(
            username="test",
            password="hello_world",
            email="test@test.com",
            first_name="hello",
            last_name="world"
        )

        self.data = {
            "email":"a@a.com",
            "funnel_entry_point": "URI: test, location: test"
        }

        self.drip_subscriber = DripSubscriber.objects.create(
            email="test@test.com",
            funnel_entry_point="unit test"
        )

        self.drip_subscriber_list = DripSubscriberList.objects.create(
            name="test list"
        )

        self.create_drip_subscriber_list_form_data = {
            "name":"test"
        }

        self.update_drip_subscriber_list_form_data = {
            "name": "updated name",
            "id": self.drip_subscriber_list.id
        }

        self.drip_message = DripMessage.objects.create(
            title="test",
            body="test message",
            author=self.user
        )


    def test_subscribe_view_does_302_redirect(self):
        response = self.client.post(reverse_lazy("subscribe"), data=self.data)
        self.assertTrue(response.status_code == 302)


    def test_subscribe_view_redirects_to_index_view(self):
        response = self.client.post(reverse_lazy("subscribe"), data=self.data)
        self.assertTrue(response.url == str(reverse_lazy("index")))


    def test_subscribe_view_does_302_redirect_to_index_view_when_email_already_exists(self):
        response = self.client.post(reverse_lazy("subscribe"), data=self.data)
        self.assertTrue(response.status_code == 302)
        
        response = self.client.post(reverse_lazy("subscribe"), data=self.data)
        self.assertTrue(response.status_code == 302)
        

    def test_subscribe_view_redirects_when_session_is_set(self):
        session = self.client.session
        session["redirect_to"] = str(reverse_lazy("featured_articles"))
        session.save()

        response = self.client.post(reverse_lazy("subscribe"), data=self.data)
        self.assertTrue(response.url == (reverse_lazy("featured_articles")))


    def test_drip_dashboard_view_redirects_when_user_not_logged_in(self):
        response = self.client.get(reverse_lazy("drip_dashboard"))
        self.assertEqual(response.status_code, 302)


    def test_drip_dashboard_view_returns_200_with_logged_in_user(self):
        logged_in = self.client.login(username="test", password="hello_world")
        response = self.client.get(reverse_lazy("drip_dashboard"))
        self.assertEqual(response.status_code, 200)


    def test_drip_subscribers_view_redirects_when_user_not_logged_in(self):
        response = self.client.get(reverse_lazy("drip_subscribers"))
        self.assertEqual(response.status_code, 302)


    def test_drip_subscribers_view_returns_200_with_logged_in_user(self):
        logged_in = self.client.login(username="test", password="hello_world")
        response = self.client.get(reverse_lazy("drip_subscribers"))
        self.assertEqual(response.status_code, 200)


    def test_drip_subscriber_status_view_redirects_when_user_not_logged_in(self):
        response = self.client.get(reverse_lazy("drip_subscriber_status", kwargs={"user_id": 99}))
        self.assertEqual(response.status_code, 302)


    def test_drip_subscriber_status_view_response_status_code_is_404_when_user_id_not_found_in_db(self):
        logged_in = self.client.login(username="test", password="hello_world")
        response = self.client.get(reverse_lazy("drip_subscriber_status", kwargs={"user_id": 99}))
        self.assertEqual(response.status_code, 404)


    def test_drip_subscriber_status_view_updates_user_subscription_status(self):
        logged_in = self.client.login(username="test", password="hello_world")
        response = self.client.get(reverse_lazy("drip_subscriber_status", kwargs={"user_id": self.drip_subscriber.id}))
        self.assertEqual(response.status_code, 302)


    def test_drip_subscriber_status_view_updates_drip_subscriber_active_field(self):
        logged_in = self.client.login(username="test", password="hello_world")
        response = self.client.get(reverse_lazy("drip_subscriber_status", kwargs={"user_id": self.drip_subscriber.id}))
        self.drip_subscriber = DripSubscriber.objects.get(email="test@test.com")
        
        self.assertFalse(self.drip_subscriber.active)

        # request above should have set active field to False
        # set it now to True

        response = self.client.get(reverse_lazy("drip_subscriber_status", kwargs={"user_id": self.drip_subscriber.id}))
        self.drip_subscriber = DripSubscriber.objects.get(email="test@test.com")
        
        self.assertTrue(self.drip_subscriber.active)


    def test_drip_subscriber_lists_view_redirects_when_user_not_logged_in(self):
        response = self.client.get(reverse_lazy("drip_subscriber_lists"))
        self.assertEqual(response.status_code, 302)


    def test_drip_subscriber_lists_view_returns_200_status_code_with_logged_in_user(self):
        logged_in = self.client.login(username="test", password="hello_world")
        response = self.client.get(reverse_lazy("drip_subscriber_lists"))
        self.assertEqual(response.status_code, 200)


    def test_drip_subscriber_list_subscribers_view_redirects_when_user_not_logged_in(self):
        response = self.client.get(reverse_lazy("drip_subscriber_list_subscribers", kwargs={"drip_subscriber_list_id": self.drip_subscriber_list.id}))
        self.assertEqual(response.status_code, 302)


    def test_drip_subscriber_list_subscribers_view_returns_200_status_code_with_logged_in_user(self):
        logged_in = self.client.login(username="test", password="hello_world")
        response = self.client.get(reverse_lazy("drip_subscriber_list_subscribers", kwargs={"drip_subscriber_list_id": self.drip_subscriber_list.id}))
        self.assertEqual(response.status_code, 200)


    def test_create_drip_subscriber_list_view_redirects_when_user_not_logged_in(self):
        response = self.client.get(reverse_lazy("drip_subscriber_lists"))
        self.assertEqual(response.status_code, 302)


    def test_create_drip_subscriber_list_redirects_to_drip_subscriber_lists_on_success(self):
        logged_in = self.client.login(username="test", password="hello_world")
        response = self.client.post(reverse_lazy("create_drip_subscriber_list"), data=self.create_drip_subscriber_list_form_data)
        self.assertTrue(response.url == str(reverse_lazy("drip_subscriber_lists")))


    def test_create_drip_subscriber_list_redirects_to_index_on_failure(self):
        logged_in = self.client.login(username="test", password="hello_world")
        response = self.client.post(reverse_lazy("create_drip_subscriber_list"), data={})
        self.assertTrue(response.url == str(reverse_lazy("drip_subscriber_lists")))


    def test_update_drip_subscriber_list_view_redirects_when_user_not_logged_in(self):
        response = self.client.get(reverse_lazy("update_drip_subscriber_list"))
        self.assertEqual(response.status_code, 302)


    def test_update_drip_subscriber_list_redirects_to_drip_subscriber_lists_on_success(self):
        logged_in = self.client.login(username="test", password="hello_world")
        response = self.client.post(reverse_lazy("update_drip_subscriber_list"), data=self.update_drip_subscriber_list_form_data)
        self.assertTrue(response.url == str(reverse_lazy("drip_subscriber_lists")))


    def test_update_drip_subscriber_list_redirects_to_index_on_failure(self):
        logged_in = self.client.login(username="test", password="hello_world")
        response = self.client.post(reverse_lazy("update_drip_subscriber_list"), data={})
        self.assertTrue(response.url == str(reverse_lazy("drip_subscriber_lists")))


    def test_delete_drip_subscriber_list_view_redirects_when_user_not_logged_in(self):
        response = self.client.get(reverse_lazy("delete_drip_subscriber_list", kwargs={"drip_subscriber_list_id": self.drip_subscriber_list.id}))
        self.assertEqual(response.status_code, 302)


    def test_delete_drip_subscriber_list_subscribers_view_redirects_when_user_not_logged_in(self):
        response = self.client.get(reverse_lazy("delete_drip_subscriber_list", kwargs={"drip_subscriber_list_id": self.drip_subscriber_list.id}))
        self.assertEqual(response.status_code, 302)


    def test_delete_drip_subscriber_list_subscribers_view_returns_302_status_code_with_logged_in_user(self):
        logged_in = self.client.login(username="test", password="hello_world")
        response = self.client.get(reverse_lazy("delete_drip_subscriber_list", kwargs={"drip_subscriber_list_id": self.drip_subscriber_list.id}))
        self.assertEqual(response.status_code, 302)


    def test_drip_messages_view_redirects_when_user_not_logged_in(self):
        response = self.client.get(reverse_lazy("drip_messages"))
        self.assertEqual(response.status_code, 302)


    def test_drip_messages_view_returns_200_status_code_with_logged_in_user(self): 
        logged_in = self.client.login(username="test", password="hello_world")
        response = self.client.get(reverse_lazy("drip_messages"))
        self.assertEqual(response.status_code, 200)


    def test_drip_message_view_redirects_when_user_not_logged_in(self):
        response = self.client.get(reverse_lazy("drip_message", kwargs={"message_id": self.drip_message.id}))
        self.assertEqual(response.status_code, 302)


    def test_drip_message_view_returns_200_status_code_with_logged_in_user(self):
        logged_in = self.client.login(username="test", password="hello_world")
        response = self.client.get(reverse_lazy("drip_message", kwargs={"message_id": self.drip_message.id}))
        self.assertEqual(response.status_code, 200)


class DripSubscriberFormUnitTest(TestCase):
    """
    Test the actual DripSubscriberForm
    and not the view
    """


    def test_drip_subscriber_form(self):
        data = {
            "email":"a@a.com",
            "funnel_entry_point":"URI: test, location: test"
        }
        form = DripSubscriberForm(data=data)
        self.assertTrue(form.is_valid())


class CreateDripSubscriberListFormUnitTest(TestCase):
    """
    Test CreateDripSubscriberListForm
    """


    def test_create_drip_subscriber_list_form(self):
        data = {
            "name": "test"
        }

        form = CreateDripSubscriberListForm(data=data)
        self.assertTrue(form.is_valid())


class UpdateDripSubscriberListFormUnitTest(TestCase):
    """
    Test UpdateDripSubscriberListForm
    """


    def test_update_drip_subscriber_list_form(self):
        data = {
            "name": "test",
            "drip_subscriber_list_id": 1
        }

        form = UpdateDripSubscriberListForm(data=data)
        self.assertTrue(form.is_valid())


class EmailSingleDripSubscriberFormUnitTest(TestCase):
    """
    Test EmailSingleDripSubscriberForm
    """


    def test_email_single_drip_subscriber_form(self):
        data = {
            "email": "a@a.com",
            "subject": "test",
            "message": "test message"
        }

        form = EmailSingleDripSubscriberForm(data=data)
        self.assertTrue(form.is_valid())


class DripTrackingUnitTest(TestCase):
    """
    Test drip.tracking
    utilities
    """


    def test_tracking_string_is_formatted_correctly(self):
        self.assertEqual(
            tracking_string(
                uri=reverse_lazy("index"),
                location="test"
            ),
            "URI /, Location: test"
        )
