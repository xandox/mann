# MANN

CMake scripts for easy starting.


## Gettings started

```
git clone https://github.com/xandox/mann.git MyProject
cd MyProject
rm -rf .git README.md
```
Set project name in CMakeLists.txt and main namespace in `project_layout.cmake`. Add dependencies to deps.cmake. That's it.

## Project layout

This screpts assume that one project is directory with own `CMakeList.txt` and at least `src` directory (or how you configured it in `project_laytout.cmake`). Of caouse it can contans other directoris for your own.

## Macros
Macros started with `_mann` is for private useg only. Try to avoid calling it.

### `mann_recursive`
Adds all directories build tree. If `MANN_CREATE_MISSING_FILES` enabled creats not exists directories with layout from `project_laytout.cmake`.
#### example
```
mann_recursive(
    base_lib_1
    base_lib_2
    somethgins_else
    main_program
)
```

### `mann_static_lib`
Starts declaration of new static library. Specific name can be passed with argument `NAME`. If name not specified - it will be created from path to this library. For example `CMakeLists.txt` for a library is laying by relative path according main `CMakeLists.txt` storages/dbs/sqlite, so name will be `PROJECT_NAEM-storages-dbs-sqlite`.

### `mann_shared_lib`
Starts declaration of new static library. Nameing the same like in static library.

### `mann_program`
Starts declartion of new executable. Nameing the same like in static library.

### `mann_includes`
Adds includes to current target. Path to include file could be absolute (for example generated in `CMAKE_BINARY_DIR` in some way) or relative. If path relative it relates to target internal include directory. External include directory is absolute path to `include` folder (see `project_layout.cmake`). Internal include directory is path in `include` directory and it build by the same rools like a naming.

### `mann_src`
Adds source to target. Path to source file could be absolute or relative. If path releative it relates to `src` directory.

### `mann_link`
Adds link dependencies. Targets only sutable. Could be PUBLIC or PRIVATE and have the same semantic (https://cmake.org/cmake/help/v3.9/command/target_link_libraries.html#id3)

### `mann_tests`
Adds tests source directory. Google tests only sutable.

### `mann_end`
Finish declartaion of target.

### `mann_configure_internal_header`
TODO
### `mann_parse_version`
TODO
