from bridge import Bridge


class Adapter:
    base_url = 'https://sandbox.swift.com/swift-apitracker/v4/payments'    # '/{uetr}/status' needs to be appended
    from_params = ['base', 'UETR', 'transaction']
    action_params = ['cancellation', 'status', 'transactions']
    oauth_token = ['oauth', 'token', 'oauth_token']

    def __init__(self, input):
        self.id = input.get('id', '1')
        self.request_data = input.get('data')
        if self.validate_request_data():
            self.bridge = Bridge()
            self.set_params()
            self.create_request()
        else:
            self.result_error('No data provided')

    def validate_request_data(self):
        if self.request_data is None:
            return False
        if self.request_data == {}:
            return False
        return True

    def set_params(self):
        for param in self.from_params:
            self.from_param = self.request_data.get(param)
            if self.from_param is not None:
                break
        for param in self.action_params:
            self.to_param = self.request_data.get(param)
            if self.to_param is not None:
                break
        for param in self.oauth_token:
            self.oauth = self.request_data.get(param)
            if self.oauth is not None:
                break

    def create_request(self):
        try:
            #
            headers = {"Authorization": "Basic "+self.oauth}
            self.base_url += "/"+self.from_param+"/"+self.to_param
            #
            response = self.bridge.request(self.base_url, headers)
            data = response.json()

            # self.result = data[self.to_param]
            self.result = data["return"] # might need to switch to ''
            data['result'] = self.result
            self.result_success(data)

        except Exception as e:
            self.result_error(e)
        finally:
            self.bridge.close()

    def result_success(self, data):
        self.result = {
            'jobRunID': self.id,
            'data': data,
            'result': self.result,
            'statusCode': 200,
        }

    def result_error(self, error):
        self.result = {
            'jobRunID': self.id,
            'status': 'errored',
            'error': f'There was an error: {error}',
            'statusCode': 500,
        }