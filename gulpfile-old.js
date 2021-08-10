var less = require('gulp-less');
var gulp = require('gulp')
var path = require('path');
gulp.task('index', function () {
    return gulp.src('index.less')
    .pipe(less({
      paths: [ path.join(__dirname, 'less', 'includes')  ]
    }))
    .pipe(gulp.dest('./'));
});

gulp.task('valentine', function () {
    return gulp.src('valentine.less')
    .pipe(less({
      paths: [ path.join(__dirname, 'less', 'includes')  ]
    }))
    .pipe(gulp.dest('./'));
});
gulp.task('watch', function() {
  gulp.watch('index.less', ['index']);
  gulp.watch('valentine.less', ['valentine']);
});
gulp.task('default', ['watch', 'index', 'valentine']);
