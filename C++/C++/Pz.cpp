#include <iostream>
#include <iostream> //класс для организации ввода-вывода
#include <Windows.h> // класс для определений типов данных, макросов, прототипов функций, констант и т.д.
#include <cmath>// класс для математических вычислений
int main()
{	
	using namespace std;
	SetConsoleCP(1251); // установка кодовой страницы win-cp 1251 в поток ввода
	SetConsoleOutputCP(1251); // установка кодовой страницы win-cp 1251 в поток вывода
	int NumS;
	cout << "Введи число от 1 до 3 ";
	cin >> NumS;
	switch (NumS)
	{

	case 1:
		try {
			int number;
			cout << "Введи трехзначное число: ";
			cin >> number;
			if (number < 100 or number > 999) {
				throw(number);
			}
			else {
				int S = (number / 100) + ((number / 10) % 10) * 10 + (number % 10) * 100;
				cout << "Число наоборот: ";
				cout << S << endl;
			}
		}
		catch (int num) {
			cout << "Ваше число:  " << num << endl;
			cout << "Программа не может быть ввыполнена. Вы должны ввести трехзначное число" << endl;
			
		}
	break;
	case 2:
		int number1;
		cout << "Введи число: ";
		cin >> number1;
		if (10 < number1 && number1 < 100 && number1 % 2 == 0) {
			cout << "Данное число четное двузначное" << endl;
		}
		else {
			cout << "Данное число не четное двузначное" << endl;
		}
		break;
	case 3:
		int a;
		int b;
		int c;
		cout << "Введи первое число: ";
		cin >> a;
		cout << "Введи второе число: ";
		cin >> b;
		cout << "Введи третье число: ";
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

		