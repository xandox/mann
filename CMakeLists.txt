cmake_minimum_required(VERSION 3.9.1)

project(MyProject CXX)

include(${CMAKE_SOURCE_DIR}/cmake/mann.cmake)

mann_git_describe(VERSION)
mann_parse_version(${VERSION} MAJOR_VERSION MINOR_VERSION BUILD_NUMBER COMMIT_HASH)
message(STATUS "Building version: ${VERSION}")
message(STATUS "Major version: ${MAJOR_VERSION}")
message(STATUS "Minor version: ${MINOR_VERSION}")
message(STATUS "Build number: ${BUILD_NUMBER}")
message(STATUS "Commit hash: ${COMMIT_HASH}")


if(MANN_ENABLE_TESTS)
    message(STATUS "Tests enabled")
    enable_testing()
endif()

