
using UnityEngine;

public abstract class Transformation : MonoBehaviour {
	
	public abstract Matrix4x4 Matrix { get; }

	public Vector3 Apply(Vector3 point)
	{
		return Matrix.MultiplyPoint(point);
	}
}

// Note that Matrix4x4.MultiplyPoint has a 3D vector parameter.
// It assumes that the missing fourth coordinate is 1.
// It also takes care of the conversion back from homogeneous coordinates
// to Euclidean coordinates.