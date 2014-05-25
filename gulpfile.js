var gulp = require('gulp');

var paths = {
  libs: {
    js: [
      'bower_components/bootstrap/dist/js/*.min.js',
      'bower_components/jquery/dist/*.min.js',
    ],
    css: [
      'bower_components/bootstrap/dist/css/*.min.css',
    ],
    fonts: [
      'bower_components/bootstrap/dist/fonts/*.*',
    ]
  }
};

gulp.task('libs:update', function() {
  for (var type in paths.libs) {
    gulp.src(paths.libs[type]).pipe(
      gulp.dest('rotina/static/libs/' + type)
    );
  }
});

gulp.task('setup', ['libs:update']);

gulp.task('default', ['setup']);
