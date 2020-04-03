from testwework.api.department import Department
from testwework.utils.Utils import Utils


class TestDepartment:
    def test_list(self):
        department = Department()
        r =department.list("")
        assert r["errcode"]==0
        assert r["department"]
        print(r)
