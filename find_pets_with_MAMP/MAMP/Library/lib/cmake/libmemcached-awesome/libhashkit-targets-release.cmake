#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "libmemcached::libhashkit" for configuration "Release"
set_property(TARGET libmemcached::libhashkit APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(libmemcached::libhashkit PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libhashkit.2.0.0.dylib"
  IMPORTED_SONAME_RELEASE "@rpath/libhashkit.2.dylib"
  )

list(APPEND _IMPORT_CHECK_TARGETS libmemcached::libhashkit )
list(APPEND _IMPORT_CHECK_FILES_FOR_libmemcached::libhashkit "${_IMPORT_PREFIX}/lib/libhashkit.2.0.0.dylib" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
