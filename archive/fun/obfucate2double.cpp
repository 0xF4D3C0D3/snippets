#include <iostream>
#include <random>

using namespace std;

void obfuscate2double(const char obfuscatedString[], int stringCount, double*& obfuscatedDouble, int& doubleCount) {
	random_device rd;
	mt19937 gen(rd());
	uniform_int_distribution<> pickRandom(3, 7);

	int currentPosition = 0;
	int sizePiece, sizeDouble = 0;
	char* stringPiece = nullptr;
	double** tempDouble = new double*[256];
	double epsilon = numeric_limits<double>::min();

	while (currentPosition < stringCount) {
		sizePiece = stringCount - currentPosition < 7 ? stringCount - currentPosition : pickRandom(gen);
		stringPiece = new char[sizePiece];
		strncpy(stringPiece, obfuscatedString + currentPosition, sizePiece);
		stringPiece[sizePiece] = '\0';

		tempDouble[sizeDouble] = reinterpret_cast<double*>(stringPiece);

		if (fabs(*(tempDouble[sizeDouble])) < epsilon) {
			continue;
		}
		currentPosition += sizePiece;
		sizeDouble++;
	}

	doubleCount = sizeDouble;
	obfuscatedDouble = new double[sizeDouble];
	for (int i = 0; i < sizeDouble; i++)
		obfuscatedDouble[i] = *tempDouble[i];
}

int main() {

	char* originalString = "Hello world! This is a test message.";
	double* obfuscatedDouble;
	int obfuscatedDoubleSize;

	obfuscate2double(originalString, strlen(originalString), obfuscatedDouble, obfuscatedDoubleSize);

	for (int i = 0; i < obfuscatedDoubleSize; i++)
		printf("%.*e\t%s\n", DECIMAL_DIG, obfuscatedDouble[i], &obfuscatedDouble[i]);

	return EXIT_SUCCESS;
}
