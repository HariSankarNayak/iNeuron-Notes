 app = angular.module("myapp", [])
 .config(['$interpolateProvider', function($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
  }])
  .controller("courseCtl", function($scope,$rootScope, $http) {
            $scope.getCourseDetails = function () {
                $http.get("/fetchCoursedetails")
                .then(function(response){

                    if(response.data != null && response.data != "null" && response.data.length > 0){
                        $scope.details = response.data;
                        console.log($scope.details )
                    }else{
                            Swal.fire({
                              title: 'Please confirm to start scraping!',
                            }).then((result) => {
                              if (result.isConfirmed) {
                                  $scope.startScaping()
                              }
                            });
                    }

                });
            }

            $scope.getCourseDetails()

            $scope.viewCourseDetails =  function(course_Detail){
                    url_slug = course_Detail.url_slug
                    url_slug = url_slug.split("/")
                    url_course = url_slug[url_slug.length-1]
                    $rootScope.course_name = url_course
                    window.location.href = "/view-course?c_name="+url_course
            }

             $scope.startScaping = function () {
                $http.get("/callParser")
                .then(function(response){
                    if(response.data != null && response.data != "null"){
                        if(response.data.status == "1"){
                             $scope.getCourseDetails()
                        }
                    }
                });
            }

 })

 app.controller("course_detailCtl", function($scope,$rootScope,$http) {
            c_name = window.location.search.split('=')[1]
            $scope.getCourseDetails = function () {
                payload = {
                   "courseName" : c_name
                }
                $http({
                    method: "POST",
                    data: payload,
                    url: "/fetchCoursedetailsWithCourseName",
                    headers: {
                        'Content-Type': "application/json"
                    }
                }).then(function(response){
                    if(response.data != null && response.data != "null"){
                        console.log(response.data)
                        $scope.c_details = response.data;
                        $scope.data = $scope.c_details.props.pageProps.data
                       $scope.inst_id = $scope.data.meta.overview.instructors
                    }else{
                            Swal.fire({
                              title: 'No data was found for this course, Web Scraping still in progress, try again after some time!',
                            }).then((result) => {
                              /* Read more about isConfirmed, isDenied below */
                              if (result.isConfirmed) {
                                    window.location.href = "/"
                              } else if (result.isDenied) {
                                    window.location.href = "/"
                              }
                            });
                    }
                });
            }

            $scope.getCourseDetails()

 });