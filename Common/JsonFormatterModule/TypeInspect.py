from inspect import isclass, getattr_static
from typing import TypeVar, get_origin, List, Dict, Optional, get_type_hints


class TypeInspect:
    __cached_annotations: Dict[type, dict] = dict()
    __cached_generic_types: Dict[type, type] = dict()

    @classmethod
    def get_annotations(cls, inspected_type: type) -> dict:
        if inspected_type in cls.__cached_annotations:
            return cls.__cached_annotations[inspected_type]

        full__ann = TypeInspect.__get_full_annotations(inspected_type)
        TypeInspect.__set_generic_types(inspected_type, full__ann)

        cls.__cached_annotations[inspected_type] = full__ann
        return full__ann

    # noinspection PyDeepBugsSwappedArgs
    @staticmethod
    def has_any_subclass(types: tuple, subclass: type):
        for t in types:
            if issubclass(t, subclass) and isclass(t):
                return True
        return False

    @staticmethod
    def __get_full_annotations(cls: type) -> Optional[dict]:
        origin = get_origin(cls)  # get class instead of _GenericAlias
        if origin is not None:
            cls = origin
        if not hasattr(cls, "__annotations__"):
            return None
        annotation: dict = get_type_hints(cls)
        if hasattr(cls, "__bases__"):
            bases = cls.__bases__
            for b in bases:
                b_ann = TypeInspect.__get_full_annotations(b)
                if b_ann:
                    annotation.update(b_ann)
        return annotation

    @staticmethod
    def __set_generic_types(cls: type, annotations: dict) -> None:
        for n, v in annotations.items():
            if type(v) is TypeVar:
                annotations[n] = TypeInspect.__get_generic_type(cls)
                continue
            origin_v = get_origin(v)
            if origin_v is not None:
                if issubclass(origin_v, List) and type(v.__args__[0]) is TypeVar:
                    generic_type = TypeInspect.__get_generic_type(cls)
                    v.__args__ = (generic_type,)  # make List[~T] to List[generic_type]
                if issubclass(origin_v, Dict) and type(v.__args__[1]) is TypeVar:
                    generic_type = TypeInspect.__get_generic_type(cls)
                    v.__args__ = (v.__args__[0], generic_type)  # make Dict[Any, ~T] to Dict[Any, genericType]

    @classmethod
    def __get_generic_type(cls, cls_type: type) -> type:
        if cls_type in cls.__cached_generic_types:
            return cls.__cached_generic_types[cls_type]

        if get_origin(cls_type) is not None:
            generic_type = cls_type.__dict__.get("__args__")[0]
            cls.__cached_generic_types[cls_type] = generic_type
            return generic_type

        generic_type = getattr_static(cls_type, "__orig_bases__")[0].__dict__.get("__args__")[0]
        cls.__cached_generic_types[cls_type] = generic_type
        return generic_type

    @classmethod
    def object_has_same_type(cls, value, expected_type: type):
        real_type = type(value)
        origin_real_type = get_origin(real_type)
        origin_expected_type = get_origin(expected_type)

        if origin_real_type is not None and origin_expected_type is None:
            return origin_real_type is expected_type

        if origin_real_type is None and origin_expected_type is not None:
            return real_type is origin_expected_type

        if origin_real_type is not None and origin_expected_type is not None:
            real_generic_type = cls.__get_generic_type(real_type)
            real_expected_type = cls.__get_generic_type(expected_type)
            return origin_real_type is origin_expected_type and real_generic_type is real_expected_type

        return real_type is expected_type
