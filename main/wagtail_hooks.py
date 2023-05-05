import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import (
    InlineStyleElementHandler, BlockElementHandler
)
from wagtail import hooks


@hooks.register("register_rich_text_features")
def register_centertext_feature(features):
    """Creates centered text in our richtext editor and page."""

    # Step 1
    feature_name = "SH"
    type_ = "SUBHEADING"
    tag = "div"

    # Step 2
    control = {
        "type": type_,
        "label": "Sub-Head",
        "description": "Adds a subheading",
        "style": {
            "font-weight": "bold"
        }
    }

    # Step 3
    features.register_editor_plugin(
        "draftail", feature_name, draftail_features.InlineStyleFeature(control)
    )

    # Step 4
    db_conversion = {
        "from_database_format": {tag: InlineStyleElementHandler(type_)},
        "to_database_format": {
            "style_map": {
                type_: {
                    "element": tag,
                    "props": {
                        "class": "b-subhead p-link"
                    }
                }
            }
        }
    }

    # Step 5
    features.register_converter_rule("contentstate", feature_name, db_conversion)

    # Step 6, This is optional.
    features.default_features.append(feature_name)


@hooks.register("register_rich_text_features")
def register_centertext_feature(features):
    """Creates centered text in our richtext editor and page."""

    # Step 1
    feature_name = "block"
    type_ = "block"
    tag = "span"

    # Step 2
    control = {
        "type": type_,
        "label": "block",
        "description": "block",
        "style": {
        
        }
    }

    # Step 3
    features.register_editor_plugin(
        "draftail", feature_name, draftail_features.InlineStyleFeature(control)
    )

    # Step 4
    db_conversion = {
        "from_database_format": {tag: InlineStyleElementHandler(type_)},
        "to_database_format": {
            "style_map": {
                type_: {
                    "element": tag,
                    "props": {
                        "class": "b-code-txt"
                    }
                }
            }
        }
    }

    # Step 5
    features.register_converter_rule("contentstate", feature_name, db_conversion)

    # Step 6, This is optional.
    features.default_features.append(feature_name)


@hooks.register('register_rich_text_features')
def register_code_block_feature(features):
    """
    Registering the `code-block` feature, which uses the `code-block` Draft.js block type,
    and is stored as HTML with `<pre><code>` tags.
    """
    feature_name = 'code-block'
    type_ = 'code-block'

    control = {
        'type': type_,
        'label': '{}',
        'description': 'Code',
        'style': {
        'white-space': 'pre-wrap'
        }
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.BlockFeature(control)
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {
            'pre': BlockElementHandler(type_),
            'code': InlineStyleElementHandler('CODE'),
        },
        'to_database_format': {
            'block_map': {'code-block': {'element': 'code', 'wrapper': 'pre', 'props': {'class': 'b-code'}}}
        },
    })

    features.default_features.append(feature_name)

# @hooks.register('register_rich_text_features')
# def make_h1_default(features):
#     features.default_features.append('code')