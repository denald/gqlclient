import requests


class GraphQLClient:
    """
    Simple python GraphQL Client based on requests module
    """

    def __init__(self, api_url):
        self.url = api_url
        self.auth_headers = None

    def execute(self, query, variables=None, raw=False, **kwargs):
        """
        Executes requests post method and sends `query` with `variables` to GraphQL endpoint
        :param query: GraphQL query
        :param variables: GraphQL variables
        :param raw: if set to True this method will return raw response object, if False response json
        object will be returned
        :param kwargs: any params that are supported by requests module, e.g. cookies, auth,
        timeout, allow_redirects, etc.
        :return: json of response if `raw` is set to False and raw response in case raw is set to True
        """
        response = requests.post(
            self.url,
            json={'query': query, 'variables': variables},
            headers=self.auth_headers if self.auth_headers else {},
            **kwargs
        )
        return response.json() if not raw else response

    def set_auth_headers(self, auth_dict: dict = None):
        self.auth_headers = auth_dict
