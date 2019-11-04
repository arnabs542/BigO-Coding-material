# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        result = 0
        st = []
        for employee in employees:
            if employee.id == id:
                result = employee.importance
                for subordinate in employee.subordinates:
                    st.append(subordinate)
            elif employee.id in st:
                st.remove(employee.id)
                result += employee.importance
                for subordinate in employee.subordinates:
                    st.append(subordinate)
        while len(st) > 0:
            tmp = st[-1]
            st.pop()
            result += tmp.importance
        return result

                
                    
