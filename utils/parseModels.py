from sqlalchemy import Integer, String, Float, Boolean, Date, DateTime
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import class_mapper

from model import models as dbmodels

# 定义SQLAlchemy类型到Python类型的映射
SQLALCHEMY_TYPE_MAPPING = {
    Integer: "int",
    String: "string",
    Float: "float",
    Boolean: "bool",
    Date: 'date',
    DateTime: 'datetime.datetime'
}


def get_python_type(sqlalchemy_type):
    for sqlalchemy_base_type, python_type in SQLALCHEMY_TYPE_MAPPING.items():
        if isinstance(sqlalchemy_type, sqlalchemy_base_type):
            return python_type
    return 'Unknown'  # 未知类型


def get_model_info(model):
    info = {}
    mapper = class_mapper(model)
    info['class_name'] = model.__name__
    info['fields'] = []
    for column in mapper.columns:
        field_info = {
            'field_name': column.name,
            'field_type': get_python_type(column.type)
        }
        info['fields'].append(field_info)
    return info


def main():
    models = [getattr(dbmodels, attr) for attr in dir(dbmodels) if isinstance(getattr(dbmodels, attr), DeclarativeMeta)]
    classInfo = []
    for model in models:
        model_info = get_model_info(model)
        class_name = model_info['class_name']
        class_info_item = {"className": class_name}
        class_attr_str = ""
        for field in model_info['fields']:
            class_attr_str += f"+{field['field_name']}:{field['field_type']} "
        class_info_item["classAttr"] = class_attr_str
        classInfo.append(class_info_item)
    with open('classInfo.py', 'w') as outfile:
        outfile.write(str(classInfo))


if __name__ == "__main__":
    main()
