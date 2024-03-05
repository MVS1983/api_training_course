from utils.api import GoogleMapsApi
from utils.methods_for_checking_response import Checking
"""Creating, changing and deleting new location"""


class TestCreatePlace:

    def test_create_new_place_by_using_post(self):

        print('Post method')
        result_post = GoogleMapsApi.create_new_place_by_post()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Checking.check_status_code(result_post, 200)

        print('Get-Post method')
        result_get = GoogleMapsApi.checking_location_by_get(place_id)
        Checking.check_status_code(result_post, 400)

        print('Put method')
        result_put = GoogleMapsApi.put_new_location_by_put(place_id)
        Checking.check_status_code(result_put, 200)

        print('Get-Put method')
        result_get = GoogleMapsApi.checking_location_by_get(place_id)
        Checking.check_status_code(result_get, 200)

        print('Delete method')
        result_delete = GoogleMapsApi.delete_location_by_delete(place_id)
        Checking.check_status_code(result_delete, 200)
