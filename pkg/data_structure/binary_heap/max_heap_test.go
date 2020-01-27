package binary_heap

import (
	"reflect"
	"testing"
)

func TestMaxHeap_Get(t *testing.T) {
	type fields struct {
		capacity int
	}
	tests := []struct {
		name     string
		fields   fields
		want     []int64
		wantErr  bool
		mockFunc func(heap *MaxHeap) error
	}{
		{
			name:    "Positive Case",
			fields:  fields{capacity: 10},
			want:    []int64{100, 80, 10, 9, 6, 5, 8, 7},
			wantErr: false,
			mockFunc: func(heap *MaxHeap) error {
				for _, num := range []int64{10, 9, 8, 7, 6, 5, 80, 100} {
					if err := heap.Insert(num); nil != err {
						return err
					}
				}

				return nil
			},
		},
		{
			name:    "Negative Case - Capacity Overflow",
			fields:  fields{capacity: 7},
			want:    []int64{80, 9, 10, 7, 6, 5, 8},
			wantErr: true,
			mockFunc: func(heap *MaxHeap) error {
				for _, num := range []int64{10, 9, 8, 7, 6, 5, 80, 100} {
					if err := heap.Insert(num); nil != err {
						return err
					}
				}

				return nil
			},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			h := NewMaxHeap(tt.fields.capacity)
			err := tt.mockFunc(h)

			if (nil != err) != tt.wantErr {
				t.Errorf("Get() wantErr = %v", tt.wantErr)
			}

			if got := h.Get(); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("Get() = %v, want %v", got, tt.want)
			}
		})
	}
}
