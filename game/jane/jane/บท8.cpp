/*#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
#include <time.h>
using namespace std;
int main()
{
string Filename;
ifstream InFile;
ofstream OutFile;
int Value;
srand(time(0));
cout << "Enter file name : ";
cin >> Filename;
cout << endl;
// open output file for write data
OutFile.open(Filename.c_str());
cout << "Now open file " << Filename << " for write" << endl;
// Get name from keyboard
for(int n = 1 ; n <= 10 ; n++) {
Value = rand() % 100;
cout << setw(5) << Value;
// write value( intgeter number ) to output file
OutFile << Value << " ";
}
cout << endl;
OutFile.close(); // close output file
cout << "Now close file " << Filename << ".\n\n";
// open input file for read data
InFile.open(Filename.c_str());
cout << "Now open file " << Filename << " for read." << endl;
// Read name from input file
for(int n = 1 ; n <= 10 ; n++) {
InFile >> Value;
cout << setw(5) << Value;
}
cout << endl;
InFile.close(); // close input file
cout << "Now close file " << Filename << ".\n\n";
return(0);
}

#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
using namespace std;
void GetandWrite(ofstream &OutFile);
void ReadandDisplay(ifstream &InFile);
int main()
{
string Filename;
ifstream InFile;
ofstream OutFile;
cout << "Enter file name : ";
cin >> Filename;
cout << endl;
// open output file for write data
OutFile.open(Filename.c_str());
cout << "Now open file " << Filename << " for write." << endl;
GetandWrite(OutFile);
OutFile.close();
cout << "Now close file " << Filename << ".\n\n";
// open input file for read data
InFile.open(Filename.c_str());
cout << "Now open file " << Filename << " for read." << endl;
ReadandDisplay(InFile);
InFile.close();
cout << "Now close file " << Filename << ".\n\n";
return(0);
}
void GetandWrite(ofstream &OutFile)
{
string Id, Name, SurName;
int Score;
// Get data from keyboard
for(int n = 1 ; n <= 3 ; n++) {
cout << "\nStudent No. " << n << endl;
cout << "Enter Id : ";
cin >> Id;
cout << "Enter Name : ";
cin >> Name;
cout << "Enter SurName : ";
cin >> SurName;
cout << "Enter Score : ";
cin >> Score;
// write value( intgeter number ) to output file
OutFile << Id << " " << Name << " ";
OutFile << SurName << " " << Score << endl;
}
cout << endl;
}
void ReadandDisplay(ifstream &InFile)
{
string Id, Name, SurName;
int Score;
// Read name from input file
for(int n = 1 ; n <= 3 ; n++) {
// read name from input file
InFile >> Id >> Name >> SurName >> Score;
cout << Id << " " << Name << " " << SurName;
cout << " " << Score << endl;
}
cout << endl;
}*/


#include <iostream>
#include <fstream>
#include <string>
#include <iomanip>
using namespace std;
int Menu();
void AddStudent(string FN);
void DisplayStudent(string FN);
int main()
{
const string Filename = "student.dat";
ifstream InFile;
ofstream OutFile;
int c;
do {
system("cls"); // call external command
c = Menu();
switch(c)
{
case 1 : AddStudent(Filename); break;
case 2 : DisplayStudent(Filename); break;
}
} while(c != 0);
cout << "Exit program." << endl;
return(0);
}
int Menu()
{
string line(25,'=');
int Choose;
cout << "Program Add-Display Student Data\n";
cout << line << endl;
cout << ": Main Menu :\n";
cout << line << endl;
cout << ": 0 - Exit :\n";
cout << ": 1 - Add Student :\n";
cout << ": 2 - Display Student :\n";
cout << line << endl;
cout << " Enter choose : ";
cin >> Choose;
return(Choose);
}
void AddStudent(string FN)
{
// open file for write and append
ofstream OutFile(FN.c_str(), ios_base::out | ios_base::app);
if (OutFile.is_open()) {
string Id, Name;
cout << "\n Add Student \n";
cout << "Enter id : ";
cin >> Id;
cout << "Enter name : ";
cin >> Name;
// write data to file student.dat
OutFile << Id << " " << Name << endl;
OutFile.close();
char Wait;
cin.get(Wait);
cout << "\nSaved already ,Press Enter to continue";
cin.get(Wait);
}
else cout << "File could not opened." << endl;
}
void DisplayStudent(string FN)
{
ifstream InFile(FN.c_str(), ios_base::in); // open file for read
if (InFile.is_open()) {
string Id, Name;
string line(30,'=');
int n = 0;
cout << "\nList Student\n";
cout << line << endl;
cout << " No. Id Name \n";
cout << line << endl;
// read data from file student.dat
InFile >> Id >> Name;
while (!InFile.eof()) {
n = n + 1;
cout << right << setw(3) << n << " : ";
cout << left << setw(6) << Id;
cout << " " << Name << endl;
InFile >> Id >> Name;
}
InFile.close();
char Wait;
cin.get(Wait);
cout << "\nPress Enter to continue";
cin.get(Wait);
}
else cout << "File could not opened." << endl;
}



