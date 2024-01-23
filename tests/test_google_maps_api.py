from utils.api import GoogleMapsApi

"""Creating, changing and deleting new location"""


class TestCreatePlace:

    def test_create_new_place_by_using_post(self):

        print('Post method')
        result_post = GoogleMapsApi.create_new_place_by_post()
        check_post = result_post.json()
        place_id = check_post.get('place_id')

        print('Get-Post method')
        result_get = GoogleMapsApi.checking_location_by_get(place_id)

        print('Put method')
        result_put = GoogleMapsApi.put_new_location_by_put(place_id)

        print('Get-Put method')
        result_get = GoogleMapsApi.checking_location_by_get(place_id)

        print('Delete method')
        result_delete = GoogleMapsApi.delete_location_by_delete(place_id)
