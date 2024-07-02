from django import template

register = template.Library()

# @register.filter
# def changes(history_record):
#     changed_fields = {}

#     if history_record.prev_record:
#         current_instance = history_record.instance
#         prev_instance = history_record.prev_record.instance

#         # Compare each field in the model
#         for field in current_instance._meta.fields:
#             field_name = field.name
#             current_value = getattr(current_instance, field_name)
#             prev_value = getattr(prev_instance, field_name)

#             # Check if the field has changed
#             if current_value != prev_value:
#                 changed_fields[field_name] = (prev_value, current_value)

#     return changed_fields


@register.filter
def changes(history_record):
    changes_info = {
        'account_number': history_record.instance.account_number,
        'updated_by': history_record.history_user.username if history_record.history_user else 'System',  # Display 'System' if no user
        'changes': history_record.get_history_type_display
    }

    if history_record.prev_record:
        current_instance = history_record.instance
        prev_instance = history_record.prev_record.instance

        for field in current_instance._meta.fields:
            field_name = field.name
            current_value = getattr(current_instance, field_name)
            prev_value = getattr(prev_instance, field_name)

            if current_value != prev_value:
                changes_info['changes'][field_name] = (prev_value, current_value)

    return changes_info