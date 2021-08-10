var less = require('gulp-less');
var path = require('path');
var gulp = require('gulp')
function lessCompile() {
  return gulp.src('./*.less')
    .pipe(less({
      paths: [ path.join(__dirname, 'less', 'includes') ]
    }))
    .pipe(gulp.dest('./'));
}

function watchTask(){
    gulp.watch(
        ['./*.less'],
        lessCompile
    );
}


exports.watchTask = watchTask;
exports.lessc = lessCompile;
exports.default = watchTask


