import voluptuous

#
# basic validation: validates string
#
schema_basic = voluptuous.Schema({
    'apikey': str
})

print(schema_basic({'apikey': 'something'}))
print(schema_basic({'apikey': 23}))  # Raises an exception
print(schema_basic({}))   # This works as well becuase we have not specified that apikey is required

#
# apikey is required
#

schema_apikey_required = voluptuous.Schema({
    voluptuous.Required('apikey'): str
})

print(schema_apikey_required({'apikey': 'something'}))
try:
    print(schema_apikey_required({}))   # This call will raise an exception because apikey is required
except voluptuous.MultipleInvalid as e:
    print(e.error_message)
