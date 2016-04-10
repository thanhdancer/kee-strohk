<?php

use App\Assignment;
use App\Submission;
use Illuminate\Http\Request;

/*
|--------------------------------------------------------------------------
| Application Routes
|--------------------------------------------------------------------------
|
| Here is where you can register all of the routes for an application.
| It is a breeze. Simply tell Lumen the URIs it should respond to
| and give it the Closure to call when that URI is requested.
|
*/

$app->get('/', function () use ($app) {
    return view('index');
});
$app->post('api/v1/login', 'AuthController@login');
$app->get('api/v1/assignments', function () use ($app) {
	return Assignment::with('users')->get();
});
$app->get('api/v1/assignment/{id}', ['middleware' => 'auth', function (Request $request, $id) use ($app) {
	return Assignment::with(['submissions' => function ($query) use ($request) {
		$query->where('user_id', $request->user()->id);
	}])->find($id);
}]);
$app->put('api/v1/assignment/{id}/submissions', ['middleware' => 'auth', function (Request $request, $id) use ($app) {
	$assignment = Assignment::find($id);
	if ($assignment->submissions()->where('finished', false)->count() > 0) {
		return $assignment->submissions()->where('finished', false)->first();
	}
	return $assignment->submissions()->create([
		'content' => null,
		'finished' => false,
		'user_id' => $request->user()->id
	]);
}]);
$app->get('api/v1/submission/{id}/edit', ['middleware' => 'auth', function (Request $request, $id) use ($app) {
	return Submission::with('assignment', 'user')->find($id);
}]);
$app->post('api/v1/submission/{id}/finish', ['middleware' => 'auth', function (Request $request, $id) use ($app) {
	$submission = Submission::find($id);
	$submission->update($request->only('keys', 'content'));
	return $submission;
}]);

