import uuid

my_id = uuid.UUID(bytes_le=uuid.uuid4().bytes_le, is_safe=uuid.SafeUUID.safe)

print(my_id)
print(my_id.is_safe)
