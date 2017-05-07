var gulp = require('gulp');
var coffee = require('gulp-coffee');
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var uglify = require('gulp-uglify');
var imagemin = require('gulp-imagemin');
var sourcemaps = require('gulp-sourcemaps');
var del = require('del');

var paths = {
  scripts: ['static/js/**/*.coffee', '!client/external/**/*.coffee'],
  images: 'client/img/**/*'
};

gulp.task('js', function() {
	gulp.src('static/src/js/*.js')
	.pipe(uglify())
	.pipe(sourcemaps.write())
	.pipe(gulp.dest('static/js'))
});

// Not all tasks need to use streams
// A gulpfile is just another node program and you can use any package available on npm
gulp.task('clean', function() {
  // You can use multiple globbing patterns as you would with `gulp.src`
  return del(['build']);
});

gulp.task('scripts', ['clean'], function() {
  // Minify and copy all JavaScript (except vendor scripts)
  // with sourcemaps all the way down
  return gulp.src(paths.scripts)
    .pipe(sourcemaps.init())
      .pipe(coffee())
      .pipe(uglify())
      .pipe(concat('all.min.js'))
    .pipe(sourcemaps.write())
    .pipe(gulp.dest('static/js'));
});

// Copy all static images
gulp.task('images', ['clean'], function() {
  return gulp.src(paths.images)
    // Pass in options to the task
    .pipe(imagemin({optimizationLevel: 5}))
    .pipe(gulp.dest('static/images'));
});

gulp.task('sass', function () {
 return gulp.src('./static/src/sass/**/*.scss')
   .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
   .pipe(gulp.dest('./static/styles'));
});

/**
 * Copy any needed files.
 *
 * Do a 'gulp copyfiles' after bower updates
 */
gulp.task("copyfiles", function() {

    gulp.src("./node_modules/bootstrap-sass/assets/fonts/bootstrap/**")
        .pipe(gulp.dest("static/fonts"));

    gulp.src("./node_modules/font-awesome/fonts/**")
        .pipe(gulp.dest("static/fonts"));
});


// Rerun the task when a file changes
gulp.task('watch', function() {
  gulp.watch(paths.scripts, ['scripts']);
  gulp.watch('./sass/**/*.scss', ['sass']);
  gulp.watch(paths.images, ['images']);
});

// The default task (called when you run `gulp` from cli)
gulp.task('default', ['watch', 'scripts', 'images']);
gulp.task('production', ['copyfiles', 'sass', 'scripts', 'images']);