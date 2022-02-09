import os
import yaml

from asyncapi.model.v2_3_0 import AsyncAPI

ASYNCAPI_SPEC_FILENAME = "sample.yaml"


class AsyncAPIModel(AsyncAPI):

    def load_from_file(filename):
        unresolved_data = AsyncAPIModel.load_data_from_file(filename)
        data = AsyncAPIModel.resolve_external_references(unresolved_data, os.path.dirname(filename))
        return AsyncAPIModel.parse_obj(data)

    @staticmethod
    def load_data_from_file(filename):
        # Currently only load data from YAML files
        with open(filename) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data

    @staticmethod
    def resolve_external_references(data, files_folder):
        if isinstance(data, dict):
            for key, value in data.items():
                if key == '$ref' and not value.startswith("#/components") and value.endswith(".yaml"):
                    data = AsyncAPIModel.resolve_external_references(AsyncAPIModel.load_data_from_file(os.path.join(files_folder, value)), files_folder)
                else:
                    data[key] = AsyncAPIModel.resolve_external_references(value, files_folder)
        elif isinstance(data, list):
            for index, value in enumerate(data):
                data[index] = AsyncAPIModel.resolve_external_references(value, files_folder)
        return data


if __name__ == "__main__":
    m = AsyncAPIModel.load_from_file(ASYNCAPI_SPEC_FILENAME)
    print("ASYNCAPI MODEL: ", m)

