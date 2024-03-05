from utils.api import GoogleMapsApi
from utils.methods_for_checking_response import Checking
from utils.logger import Logger
"""Creating, changing and deleting new location"""


class TestCreatePlace:

    def test_create_new_place_by_using_post(self):

        print('\nPost method')
        result_post = GoogleMapsApi.create_new_place_by_post()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_post, 200)
        Checking.check_json_field(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_value(result_post, 'status', 'OK')

        print('Get-Post method')
        result_get = GoogleMapsApi.checking_location_by_get(place_id)
        Checking.check_status_code(result_post, 200)
        Checking.check_json_field(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                               'website', 'language'])
        Checking.check_json_value(result_get, 'language', 'French-IN')

        print('Put method')
        result_put = GoogleMapsApi.put_new_location_by_put(place_id)
        print(result_put.text)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_field(result_put, ['msg'])
        Checking.check_json_value(result_put, 'msg', 'Address successfully updated')

        print('Get-Put method')
        result_get = GoogleMapsApi.checking_location_by_get(place_id)
        print(list(result_get.json()))
        Checking.check_status_code(result_get, 200)
        Checking.check_json_field(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                               'website', 'language'])
        Checking.check_json_value(result_get, 'address', '100 Lenina street, RU')

        print('Delete method')
        result_delete = GoogleMapsApi.delete_location_by_delete(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_field(result_delete, ['status'])
        Checking.check_json_value(result_delete, 'status', 'OK')

        print('Get-Delete method')
        result_get = GoogleMapsApi.checking_location_by_get(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_field(result_get, ['msg'])
        Checking.check_json_certain_value(result_get, 'msg', 'failed')

        print("Testing of creating, changing and deleting a new location was successful.")
