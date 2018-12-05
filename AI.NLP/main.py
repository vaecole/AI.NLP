from lecture4 import edit_distance
from lecture4 import rob_cutting

print(rob_cutting.revenue_cache(20))
print(rob_cutting.revenue_lru(20))
print(rob_cutting.revenue_memo(20))

print(edit_distance.get_edit_distance("little cutie", "a little cuty"))
