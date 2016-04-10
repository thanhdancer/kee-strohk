<?php

namespace App;

use Illuminate\Database\Eloquent\Model;

class Assignment extends Model
{
    /**
     * The attributes that are mass assignable.
     *
     * @var array
     */
    protected $fillable = [
        'name', 'description', 'content'
    ];

    public function users()
    {
        return $this->belongsToMany(User::class, 'submissions');
    }

    public function submissions()
    {
        return $this->hasMany(Submission::class);
    }
}
