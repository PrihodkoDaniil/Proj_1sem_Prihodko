#include <iostream>
#include <iostream> //����� ��� ����������� �����-������
#include <Windows.h> // ����� ��� ����������� ����� ������, ��������, ���������� �������, �������� � �.�.
#include <cmath>// ����� ��� �������������� ����������
int main()
{	
	using namespace std;
	SetConsoleCP(1251); // ��������� ������� �������� win-cp 1251 � ����� �����
	SetConsoleOutputCP(1251); // ��������� ������� �������� win-cp 1251 � ����� ������
	int NumS;
	cout << "����� ����� �� 1 �� 3 ";
	cin >> NumS;
	switch (NumS)
	{

	case 1:
		try {
			int number;
			cout << "����� ����������� �����: ";
			cin >> number;
			if (number < 100 or number > 999) {
				throw(number);
			}
			else {
				int S = (number / 100) + ((number / 10) % 10) * 10 + (number % 10) * 100;
				cout << "����� ��������: ";
				cout << S << endl;
			}
		}
		catch (int num) {
			cout << "���� �����:  " << num << endl;
			cout << "��������� �� ����� ���� ����������. �� ������ ������ ����������� �����" << endl;
			
		}
	break;
	case 2:
		int number1;
		cout << "����� �����: ";
		cin >> number1;
		if (10 < number1 && number1 < 100 && number1 % 2 == 0) {
			cout << "������ ����� ������ ����������" << endl;
		}
		else {
			cout << "������ ����� �� ������ ����������" << endl;
		}
		break;
	case 3:
		int a;
		int b;
		int c;
		cout << "����� ������ �����: ";
		cin >> a;
		cout << "����� ������ �����: ";
		cin >> b;
		cout << "����� ������ �����: ";
		cin >> c;
		if (a < b && b < c) {
			a = a * 2;
			b = b * 2;
			c = c * 2;
			cout << "-----------------" << endl;
			cout << a << endl;
			cout << b << endl;
			cout << c << endl;
		}
		else {
			a = a * (-1);
			b = b * (-1);
			c = c * (-1);
			cout << "-----------------" << endl;
			cout << a << endl;
			cout << b << endl;
			cout << c << endl;;
		}
		break;
	}
		return 0;
}

		