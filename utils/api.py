from utils.http_methods import HttpMethods
from utils.jsons import json_creating_new_place

"""Testing methods for api"""
base_url = 'https://rahulshettyacademy.com'
post_resource = '/maps/api/place/add/json'
get_resource = '/maps/api/place/get/json'
put_resource = '/maps/api/place/update/json'
delete_resource = '/maps/api/place/delete/json'
key = '?key=qaclick123'  # param for all requests


class GoogleMapsApi:

    @staticmethod
    def create_new_place_by_post():
        """Creating new location method"""

        post_url = f'{base_url}{post_resource}{key}'
        print(post_url)
        result_post = HttpMethods.post(post_url, json_creating_new_place)
        print(result_post.text)
        return result_post

    @staticmethod
    def checking_location_by_get(place_id):
        """Checking new location method"""

        get_url = f'{base_url}{get_resource}{key}&place_id={place_id}'
        print(get_url)
        result_get = HttpMethods.get(get_url)
        print(result_get.text)
        return result_get

    @staticmethod
    def put_new_location_by_put(place_id):
        """Checking new location method"""

        json_for_updating = {
            "place_id": place_id,
            "address": "100 Lenina street, RU",
            "key": "qaclick123"
        }
        put_url = f'{base_url}{put_resource}{key}'
        print(put_url)
        result_put = HttpMethods.put(put_url, json_for_updating)
        print(result_put.text)
        return result_put

    @staticmethod
    def delete_location_by_delete(place_id):
        """Location delete method"""

        json_for_deleting = {
            "place_id": place_id,

        }
        delete_url = f'{base_url}{delete_resource}{key}'
        print(delete_url)
        result_delete = HttpMethods.delete(delete_url, json_for_deleting)
        print(result_delete.text)
        return result_delete
