# -*- mode:python; coding:utf-8 -*-

# Copyright (c) 2020 IBM Corp. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Validate by confirming no duplicate items."""

from trestle.core.base_model import OscalBaseModel
from trestle.core.validator import Validator
from trestle.core.validator_helper import has_no_duplicate_values_by_name


class DuplicatesValidator(Validator):
    """Check for duplicate items in oscal object."""

    def model_is_valid(self, model: OscalBaseModel) -> bool:
        """Test if the model is valid."""
        return has_no_duplicate_values_by_name(model, 'uuid')