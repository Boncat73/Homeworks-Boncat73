#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "libmemcached::p9y" for configuration "Release"
set_property(TARGET libmemcached::p9y APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(libmemcached::p9y PROPERTIES
  IMPORTED_LINK_INTERFACE_LANGUAGES_RELEASE "CXX"
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libp9y.a"
  )

list(APPEND _IMPORT_CHECK_TARGETS libmemcached::p9y )
list(APPEND _IMPORT_CHECK_FILES_FOR_libmemcached::p9y "${_IMPORT_PREFIX}/lib/libp9y.a" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
