#include <bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    cout << "Message: ";
    cin >> s;
    int key;
    while (true)
    {
        string t = "";
        cout << endl << "Enter key: ";
        cin >> key;
        for (int i = 0; i < s.size(); i++)
        {
            t += char(int(s[i] + key - 97)%26 + 97);
        }
        cout << t << endl;
    }

    return 0;
}