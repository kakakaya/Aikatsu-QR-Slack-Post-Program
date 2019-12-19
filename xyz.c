i;
main() {
	char[] a = {'j', 'p', 'g', '.', 'c', 'o', 'm'};
	for(i^=i;i < sizeof(a) / sizeof(char);++i)
		putchar(a[i]);
}

