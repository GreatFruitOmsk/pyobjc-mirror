/*
 *  This file contains type and function definitions that are helpfull for
 *  adding constants to the python module
 *
 *  NOTE: The functions are defined as 'static inline' to avoid compiler 
 *  warnings.
 *  NOTE2: The functions are not in a seperate file because I am lazy and
 *  to make using this file easier
 */
struct inttable {
	char* 	name;
	int	value;
};

struct stringtable {
	char*	  name;
	NSString* const* value;
};

#define xSTR(x) #x
#define STR(x) xSTR(x)

#define CONST_ENTRY(var) { STR(var), var }
#define STR_ENTRY(var) { STR(var), &var }
#define STR_VAR(var) if (add_string(d, STR(var), var) < 0) return
#define INT_VAR(var) if (add_int(d, STR(var), var) < 0) return

static inline int add_double(PyObject*d, char* name, double value)
{
	int res;
	PyObject* v;

	v = PyFloat_FromDouble(value);
	if (v == NULL) return -1;

	res = PyDict_SetItemString(d, name, v);
	if (res < 0) return -1;
	return 0;
}

static inline int add_float(PyObject*d, char* name, float value)
{
	int res;
	PyObject* v;

	v = PyFloat_FromDouble(value);
	if (v == NULL) return -1;

	res = PyDict_SetItemString(d, name, v);
	if (res < 0) return -1;
	return 0;
}

static inline int add_unsigned(PyObject*d, char* name, unsigned value)
{
	int res;
	PyObject* v;

	v = PyInt_FromLong(value);
	if (v == NULL) return -1;

	res = PyDict_SetItemString(d, name, v);
	if (res < 0) return -1;
	return 0;
}

static inline int add_BOOL(PyObject*d, char* name, BOOL value)
{
	int res;
	PyObject* v;

	v = PyBool_FromLong(value);
	if (v == NULL) return -1;

	res = PyDict_SetItemString(d, name, v);
	if (res < 0) return -1;
	return 0;
}

static inline int add_int(PyObject*d, char* name, int value)
{
	int res;
	PyObject* v;

	v = PyInt_FromLong(value);
	if (v == NULL) return -1;

	res = PyDict_SetItemString(d, name, v);
	if (res < 0) return -1;
	return 0;
}

static inline int register_ints(PyObject* d, struct inttable* table)
{
	while (table->name != NULL) {
		if (add_int(d, table->name, table->value) < 0) return -1;	
		table++;
	}
	return 0;
}

static inline int add_string(PyObject* d, char* name, NSString* value)
{
	int res;
	PyObject* v;

	v = ObjC_ObjCToPython("@", &value);
	if (v == NULL) return -1;

	res = PyDict_SetItemString(d, name, v);
	if (res < 0) return -1;
	return 0;
}

static inline int register_strings(PyObject* d, struct stringtable* table)
{
	while (table->name != NULL) {
		add_string(d, table->name, *table->value);
		table++;
	}
	return 0;
}

