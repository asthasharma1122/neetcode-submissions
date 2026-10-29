
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode* list3 = nullptr;
        ListNode* tail = nullptr;

        while (list1 != nullptr && list2 != nullptr) {
            int value;

            if (list1->val <= list2->val) {
                value = list1->val;
                list1 = list1->next;
            }
            else {
                value = list2->val;
                list2 = list2->next;
            }

            ListNode* newNode = new ListNode(value);

            if (list3 == nullptr) {
                list3 = newNode;
                tail = newNode;
            }
            else {
                tail->next = newNode;
                tail = tail->next;
            }
        }

        while (list1 != nullptr) {
            ListNode* newNode = new ListNode(list1->val);

            if (list3 == nullptr) {
                list3 = newNode;
                tail = newNode;
            }
            else {
                tail->next = newNode;
                tail = tail->next;
            }

            list1 = list1->next;
        }

        while (list2 != nullptr) {
            ListNode* newNode = new ListNode(list2->val);

            if (list3 == nullptr) {
                list3 = newNode;
                tail = newNode;
            }
            else {
                tail->next = newNode;
                tail = tail->next;
            }

            list2 = list2->next;
        }

        return list3;
    }
};
