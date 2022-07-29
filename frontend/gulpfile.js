const gulp = require('gulp');
const postcss = require('gulp-postcss');
const postcss_combine_duplicated_selectors = require('postcss-combine-duplicated-selectors');
const postcss_discard_duplicates = require('postcss-discard-duplicates');
const postcssPresetEnv = require('postcss-preset-env');
const autoprefixer = require('autoprefixer')

  const postcssPlugins = [
    postcss_combine_duplicated_selectors({}),
    postcss_discard_duplicates(),
    postcssPresetEnv(),
    autoprefixer({})
  ];

gulp.task('css', function () {
  return gulp
    .src('./src/app/**/*.css')
    .pipe(postcss(postcssPlugins))
    .pipe(gulp.dest('./dest'));
});

gulp.task('scss', function () {
  return gulp
    .src('./src/app/**/*.scss')
    .pipe(postcss(postcssPlugins))
    .pipe(gulp.dest('./dest'));
});

gulp.task('default', gulp.series('scss', 'css'))

